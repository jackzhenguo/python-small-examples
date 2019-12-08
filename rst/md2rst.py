
def auto_md2rst(input_file,output_file):
    try:
        my_key = 'NrtpV6kD5BdVxJ2R20eBqgCHK6heTjEMxtWSWENeZ9HdKUj5Ew3aCpodMCPPwLeH'


        import cloudconvert
        api = cloudconvert.Api(my_key)
        process = api.createProcess({
            "inputformat": "md",
            "outputformat": "rst"
        })
       
        process.start({
            "input": "upload",
            "file": open(input_file, 'rb'),
            "filename":""
        })

        process.refresh() # fetch status from API
        process.wait() # wait until conversion completed
        print(process['message']) #  access process data

        process.download(output_file)

        print("OK")
    except Exception as e:
        print(e)
        

auto_md2rst('./md/keras入门例子.md','./rst/keras入门例子.rst')