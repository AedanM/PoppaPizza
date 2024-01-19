import js2py 
print("Hello")
eval_res, tempfile = js2py.run_file("da.js") 


print(dir(eval_res))