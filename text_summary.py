import json
import os
from anthropic import AnthropicBedrock

# Define paths
input_folder = 'summary_input'
output_folder = 'final_summary'
prompt_file_path = os.path.join(input_folder, 'prompt.txt')
transcript_file_path = os.path.join(input_folder, 'output.txt')
output_file_path = os.path.join(output_folder, 'Medical_Chart.txt')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the content from prompt.txt
with open(prompt_file_path, 'r') as prompt_file:
    prompt_content = prompt_file.read()

# Escape special characters to make it JSON-compatible
escaped_prompt_content = json.dumps(prompt_content)

# Remove the surrounding quotes added by json.dumps
escaped_prompt_content = escaped_prompt_content[1:-1]

# Read the content from output.txt
with open(transcript_file_path, 'r') as output_file:
    transcript_content = output_file.read()

# Escape special characters to make it JSON-compatible
escaped_transcript_content = json.dumps(transcript_content)

# Remove the surrounding quotes added by json.dumps
escaped_transcript_content = escaped_transcript_content[1:-1]

client = AnthropicBedrock(
    # Authenticate by either providing the keys below or use the default AWS credential providers, such as
    # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    aws_access_key="AWS_ACCESS_KEY_ID",
    aws_secret_key="AWS_SECRET_ACCESS_KEY",
    # Temporary credentials can be used with aws_session_token.
    # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,
    # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
    aws_region="us-east-1",
)

message = client.messages.create(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    max_tokens=100000,
    system=escaped_prompt_content,
    messages=[
        {
            "role": "user",
            "content": f"Your job is to take the patient transcript and create a Medical Chart Documentation for the transcript in the exact format that will be placed below at the end of this prompt. Please make sure to replace any PII within the Medical Chart Documentation with [REDACTED] like stated in the example in your system prompt. You must follow the exact format for your response as you have been instructed to in your system prompt. here is the transcript: {escaped_transcript_content}"
        }
    ]
)

# Print the message content to inspect its structure
print(message.content)

# Assuming `message.content` is a list of TextBlock objects
if isinstance(message.content, list):
    response_texts = [block.text for block in message.content]
else:
    response_texts = [message.content]

# Combine the text from all TextBlock objects if there are multiple
combined_text = "\n".join(response_texts)

# # Remove special characters and formatting
clean_text = combined_text.replace("\\n", "\n").replace("\\t", "\t").replace("\\", "")

# Write the final cleaned text to Medical_Chart.txt
with open(output_file_path, 'w') as output_file:
    output_file.write(clean_text)

print("The cleaned medical chart has been saved to Medical_Chart.txt.")
