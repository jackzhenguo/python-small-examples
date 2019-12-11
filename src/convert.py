import cloudconvert

api = cloudconvert.Api(
    'NrtpV6kD5BdVxJ2R20eBqgCHK6heTjEMxtWSWENeZ9HdKUj5Ew3aCpodMCPPwLeH')

process = api.convert({
    'inputformat': 'md',
    'outputformat': 'rst',
    'input': 'upload',
    'file': open('./mytest.md', 'rb')
})
process.wait()  # wait until conversion finished
process.download("./mytest.rst")  # download output file
