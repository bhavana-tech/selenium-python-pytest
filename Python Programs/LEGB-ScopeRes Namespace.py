def top_most_dada():
    print("Most outer func")
    us_global_Big_daddy_law = "US is big daddy,i'am impregnable!"  #Global Variable


def EU_Union_outerfunction():  #Outer function
    eu_union = "Laws restricted to EU only!"  #Enclosing Variable

    print("printing only eu_union=200, entry is restricted to inner func from here is ukraine")
    list_outer = ['Hungary', 'Ireland', 'Poland']
    for i in list_outer:
        print(i)

    def local_rule():  #Inner function
        local_law = "Pakka Local"  #Local Variable

        print("printing pakka local law")
        list_inner = ['India', 'Pakistan', 'Srilanka', 'Bangla', 'Myamnar']
        for j in list_inner:
            print(j)
    local_rule()
top_most_dada()
EU_Union_outerfunction()
