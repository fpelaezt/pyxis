import boto3
import sys
 
def create_stack(stack_name = 'MyFirstVPC',file_path = '../CloudFormation/VPC-NotNAT.yml'):
#def main(stack_name, file_path):
    print("Starting stack creation")
    # open the test file from the current diectory
    template = open(file_path).read()
    # create the boto3 cloudformation client
    cloudformation = boto3.client("cloudformation")
    # create the new stack
    cloudformation.create_stack(StackName=stack_name,TemplateBody=template)
    # create the new waiter
    waiter = cloudformation.get_waiter('stack_create_complete')
    # wait until the stack state changes to "CREATE_COMPLETE"
    waiter.wait(StackName=stack_name)
    print("StackName '" + stack_name + "' was created sucessfully")

def main():
    #Create NetworkLayer
    print("Starting Network stack creation")
    create_stack('NetworkStackPyxis',file_path = '../CloudFormation/NetworkingLayer-Pyxis.yml')
    #Create ServerLayer
    print("Starting Server stack creation")
    create_stack('ServersStackPyxis',file_path = '../CloudFormation/ServersLayer-Pyxis.yml')

if __name__ == "__main__":
    main()
