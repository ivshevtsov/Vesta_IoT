

#DATA/EMIR_REPORT/em.txt
file_directory = input('Input file:')
print(file_directory)

file_result=open("DATA/EMIR_REPORT/result.txt", "w")

with open(str(file_directory), "r") as file_em:
    # итерация по строкам
    for line in file_em:
        if line.strip()[0:4]=='fail' \
                or line.strip()[0:4]=='----'\
                or line.strip()[0:4]=='avg' \
                or line.strip()[0:4]=='rms' \
                or line.strip()[0:4]=='max' \
		        or line.strip()[0:4]=='%fai'\
                or line.strip()[0:4]=='(A) ':
            #print(line.strip())
            file_result.write(line.strip()+'\n')
    file_result.close()

