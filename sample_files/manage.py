from sample_files.user_will.user_will import reaction

def manage(user_name):
    user_will = input("short report \nfull repotr \nadd \n\t")
    if user_will == 'full report':
        user_will = input('expense \nincome \ncash income \ncash expense \ncash withdrawal \nall \n\t')
    if user_will == 'add':
        user_will = 'add' + input('expense \nincome \ncash income \ncash expense \ncash withdrawal\n\t')

    reaction(user_name ,user_will)