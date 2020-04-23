import os


class Votes:

    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def countVotes(self):
        m = {}

        with open(self.__path, 'r') as f:
            i = 0
            for line in f.readlines():
                arr = line.split(',')
                arr[1] = arr[1].replace(' ', '')
                arr[1] = arr[1].replace('\n', '')
                print(int(arr[0]), int(arr[1]))
                if arr[1] not in m:
                    val = [arr[0]]
                else:
                    val.append(arr[0])
                m.update({arr[1]: val})

            sorted_map = sorted(m.items(), key=lambda x: len(x[1]), reverse=True)
            print(list(sorted_map))
            sorted_list = list(sorted_map)
            print([sorted_list[0][0], sorted_list[1][0], sorted_list[2][0]])
            # return [, sorted_map[1], sorted_map[2]]
            # for line in f.readlines():
            #     line = line.replace('\n', '')
            #     line = line.replace(' ', '')
            #     arr = line.split(',')
            #     print(arr)
            # if arr[1] not in m:
            #     m[arr[1]] = arr[0]
            # else:
            #     print(m[arr[1]])
            # m.update(m[arr[1]],a)


if __name__ == '__main__':
    print('hello')
    print(os.getcwd())
    v = Votes('votes.txt')
    print(v.countVotes())
