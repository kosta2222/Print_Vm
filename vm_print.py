import sys
b_c=[0]*40
r=0
push_i=1
push_str=2
push_fl=3
locals_=4
globals_=5
locals_len=6
globals_len=7
locals_np_shape=8
globals_np_shape=9
locals_ind_array=10
globals_ind_array=11
locals_dir=12
globals_dir=13
locals_type=14
globals_type=15
locals_help=16
globals_help=17
ops=["r","push_i","push_str","push_fl","locals","globals","locals_len","globals_len",
     "locals_np_shape","globals_np_shape","locals_ind_array","globals_ind_array","locals_dir",
     "globals_dir","locals_type","globals_type","locals_help","globals_help"]
locals_ind_array=10
def console():
    global b_c
    i=""
    splitted_cmd:list=['']*2
    main_cmd=''
    c=''
    par_cmd=''
    cmd_in_ops=''
    cn = -1
    print("Zdravstvuite ya sostavitel bait-coda dla etoi programmi")
    print("Dostupnie codi")
    for c in ops:
        print(c, end=' ')
    print()
    while True:
        i=input(">>>")
        if i=="r":
            break
        # Ищем код в списке In:i:str Out:b_c:list
        splitted_cmd_src=i.split()
        for cn1 in range(len(splitted_cmd_src)):
            splitted_cmd[cn1]=splitted_cmd_src[cn1]
        main_cmd=splitted_cmd[0]
        par_cmd=splitted_cmd[1]
        for c in range(len(ops)):
            cmd_in_ops=ops[c]
            if cmd_in_ops==main_cmd:
                cn+=1
                b_c[cn]=c
                if par_cmd!='':
                    cn+=1
                    b_c[cn]=par_cmd
            # Очищаем
            splitted_cmd[0]=''
            splitted_cmd[1]=''
        cn+1


def vm_proc_print(b_c:list,locs:dict,globs:dict):
    ip=0
    sp=-1
    sp_str=-1
    sp_fl=-1
    steck=[0]*10
    steck_fl=[0.0]*10
    steck_str=['']*10
    op=0
    op=b_c[ip]
    while True:
        if op==push_i:
            sp+=1
            ip+=1
            steck[sp]=int(b_c[ip]) # Из строкового параметра
        elif op == push_fl:
            sp_fl += 1
            ip += 1
            steck_fl[sp_fl] = float(b_c[ip])  # Из строкового параметра
        elif op==push_str:
            sp_str+= 1
            ip += 1
            steck_str[sp_str] = b_c[ip]
        elif op == r:
            break
        elif op == locals_:
          try:
            var=steck_str[sp_str]
            sp_str-=1
            label=steck_str[sp_str]
            sp_str-=1
            var_s=locs[var]
            print(label,str(var_s))
          except KeyError:
              return

        elif op == globals_:
            var = steck_str[sp_str]
            sp_str -= 1
            label = steck_str[sp_str]
            sp_str -= 1
            var_s = globs[var]
            print(label, str(var_s))
        elif op == locals_len:
          try:
            var = steck_str[sp_str]
            sp_str -= 1
            label = steck_str[sp_str]
            sp_str -= 1
            var_s = locs[var]
            var_s_len=len(var_s)
            print(label, str(var_s_len))
          except KeyError:
              return

        elif op == globals_len:
          try:
            var = steck_str[sp_str]
            sp_str -= 1
            label = steck_str[sp_str]
            sp_str -= 1
            var_s = globs[var]
            var_s_len=len(var_s)
            print(label, str(var_s_len))
          except KeyError:
              return

        elif op == locals_np_shape:
            try:
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = locs[var]
                var_s_shape=getattr(var_s,"shape")
                print(label, str(var_s_shape))
            except KeyError :
                return
        elif op == globals_np_shape:
            try:
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = globs[var]
                var_s_shape=getattr(var_s,"shape")
                print(label, str(var_s_shape))
            except KeyError:
                return
        elif op == locals_ind_array:
            try:
                ind = steck[sp]
                sp-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = locs[var]
                ind_arr=var_s[ind]
                print(label, str(ind_arr))
            except KeyError:
                return
        elif op == globals_ind_array:
            try:
                ind = steck[sp]
                sp-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = globs[var]
                ind_arr=var_s[ind]
                print(label, str(ind_arr))
            except KeyError:
                return
        elif op == locals_dir:
            try:
                sp_str-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = locs[var]
                print(label, str(dir(var_s)))
            except KeyError:
                return
        elif op == globals_dir:
            try:
                sp_str-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = globs[var]
                print(label, str(dir()))
            except KeyError:
                return
        elif op == locals_type:
            try:
                sp_str-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = locs[var]
                print(label, str(type(var_s)))
            except KeyError:
                return
        elif op == globals_type:
            try:
                sp_str-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = globs[var]
                print(label, str(type(var_s)))
            except KeyError:
                return
        elif op == locals_help:
            try:
                sp_str-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = locs[var]
                print(label, str(help(var_s)))
            except KeyError:
                return
        elif op == globals_help:
            try:
                sp_str-=1
                var = steck_str[sp_str]
                sp_str -= 1
                label = steck_str[sp_str]
                sp_str -= 1
                var_s = globs[var]
                print(label, str(help(var_s)))
            except KeyError:
                return
        else:
            print("Unknown byte-code",ops[op])
        ip+=1
        op = b_c[ip]

