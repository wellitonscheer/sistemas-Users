script_dir=$(dirname $0)

dir_output_file=$script_dir/temp/packged.yaml

aws cloudformation packged --template-file $script_dir/../cloudFormation/creatingLambdaFunction.yaml --
