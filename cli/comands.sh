script_dir=$(dirname $0)

source $script_dir/../.env

dir_output_file=$script_dir/temp/packged.yaml

aws cloudformation package --template-file $script_dir/../cloudFormation/CLsistemasUsers.yaml --s3-bucket $DeployBucketName --output-template-file $dir_output_file --region $AWS_REGION

aws cloudformation deploy --template-file $dir_output_file --stack-name sistemas-users-stack --region $AWS_REGION

cat $dir_output_file
rm -f $dir_output_file
