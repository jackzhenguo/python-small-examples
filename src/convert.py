import cloudconvert
import os
import time

api = cloudconvert.Api(
    'NrtpV6kD5BdVxJ2R20eBqgCHK6heTjEMxtWSWENeZ9HdKUj5Ew3aCpodMCPPwLeH')


def convert(input_file):
    filename, ext = os.path.splitext(input_file)
    if ext != '.md':
        return
    print(f'begin to convert {filename}...')
    process = api.convert({
        'inputformat': 'md',
        'outputformat': 'rst',
        'input': 'upload',
        'file': open('./md/{}'.format(input_file), 'rb')
    })
    process.wait()  # wait until conversion finished
    # download output file

    process.download(
        "./rst/tmp/{}.rst".format(filename))
    print(f"convert {filename} success")


i = 0
for input_file in os.listdir('./md'):
    if i < 8:
        i += 1
        continue
    convert(input_file)
    time.sleep(1)
