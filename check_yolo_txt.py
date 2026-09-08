import os


label_dir = r"D:\battery_ai\labels_temp"


error_count = 0
empty_count = 0
total = 0


for file in os.listdir(label_dir):

    if file.endswith(".txt"):

        total += 1

        path = os.path.join(
            label_dir,
            file
        )


        with open(path,"r") as f:

            lines = f.readlines()



        # 空标签

        if len(lines)==0:

            empty_count += 1
            print("空标签:",file)



        for line in lines:

            data=line.strip().split()


            # YOLO-seg至少:
            # 类别 + 3个点(x,y)

            if len(data)<7:

                print("异常:",file)
                error_count+=1
                break



            # 检查坐标范围

            coords=data[1:]


            for c in coords:

                value=float(c)

                if value<0 or value>1:

                    print("坐标异常:",file,value)

                    error_count+=1
                    break



print("================")
print("标签数量:",total)
print("空标签:",empty_count)
print("异常数量:",error_count)
print("================")