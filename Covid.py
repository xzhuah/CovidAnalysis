import matplotlib.pyplot as plt

# 病毒传播演算程序

if __name__ == '__main__':

    # 当前无感染历史人口, 数组的第n个表示第n天的情况 3/17
    N = [39560000]
    # 当前感染且未被隔离的人数
    M = [607 * 1]
    # 当前感染且已被隔离的人数
    MM = [607]
    # 已被治愈的人数，不再参与传播
    K = [10]
    # 死亡人数
    D = [11]

    # 每天隔离患者治愈和死亡的概率(每日)
    qq = 0.10
    bb = 0.0025

    # 非隔离患者的治愈和死亡概率(每日)
    q = 0.03
    b = 0.0075

    # 接触患者后的传播成功率
    p = 0.405

    # 假设未隔离的人平均每天接触a个其他未隔离的人
    a = 0.8

    # 患者隔离概率，假设前一天的患者有这么多概率被发现且受到隔离
    r = 0.4

    # 假设隔离的人平均每天接触aa个其他未隔离的人 [衡量隔离效果]
    aa = 0.01

    # 演算n天的结果
    n = 2

    # 演算开始
    for i in range(n):
        # 未被隔离的人的总数
        total_un_sep_people = N[-1] + M[-1] + K[-1]
        # 未被隔离的人是患者的概率
        prob_of_infected = M[-1] / total_un_sep_people
        # 每个人每天接触的a个未被隔离的人中有多少个患者
        touched_infected_people = a * prob_of_infected
        # 由未被隔离的患者导致的新的感染者
        new_infected_from_un_sep = touched_infected_people * p * N[-1]
        # 由于隔离不力导致的新的感染者
        new_infected_from_sep = MM[-1] * aa * p
        print(new_infected_from_un_sep, new_infected_from_sep)
        # 新的患者数量
        new_infected = new_infected_from_un_sep + new_infected_from_sep
        # 死亡的患者数量
        new_dead = MM[-1] * bb + M[-1] * b
        # 痊愈的患者数量
        healed = MM[-1] * qq + M[-1] * q
        # 新的被隔离的患者数量
        new_sep = (M[-1] - M[-1] * b - M[-1] * q) * r

        # 数据更新

        # 新的死亡人数为昨天的死亡人数累加今天新的死亡人数
        D.append(D[-1] + new_dead)
        # 新的治愈人数为昨天的治愈人数累加今天的治愈人数
        K.append(K[-1] + healed)
        # 新的隔离人数为昨天的隔离人数加今天新的隔离人数减去隔离中死亡和治愈的人数
        MM.append(MM[-1] + new_sep - MM[-1] * bb - MM[-1] * qq)
        # 新的未隔离患者人数为昨天的未隔离患者人数加新增加的未隔离患者减去未隔离中死亡和治愈的人数以及被新隔离的人数
        M.append(M[-1] + new_infected - M[-1] * b - M[-1] * q - new_sep)
        # 新的无感染历史人口为上一周期的数值减去新感染的人
        N.append(N[-1] - new_infected)

        print("Total People", D[-1] + K[-1] + MM[-1] + M[-1] + N[-1])

    # 展示演算结果
    t = range(n + 1)
    plt.plot(t, D, 'r--', t, M, 'bs', t, MM, 'g^')
    plt.show()
    # 打印报告

    print("=" * 30)

    print("流行病参数：患者每日死亡概率：{0}，每日治愈概率：{1}，通过接触成功传播的概率{2}".format(b, q, p))
    print("医疗水平参数：患者被隔离的概率：{0}， 隔离的患者每天死亡的概率：{1}，隔离的患者每天被治愈的概率：{2}，被隔离的患者每天仍然能接触的人数".format(r, bb, qq, aa))
    print("政策影响下的人口情况：普通人每天接触的人数：{0}".format(a))
    print("演算天数：{0}".format(n))

    print("=" * 30)

    print("初始情况：")
    print("死亡人数", D[0])
    print("获得免疫的人数", K[0])
    print("感染且未被隔离的人数", M[0])
    print("感染且被隔离的人数", MM[0])
    print("尚未被感染的人数", N[0])

    print("=" * 30)

    print("最终结果：")
    print("死亡人数", D[-1])
    print("获得免疫的人数", K[-1])
    print("感染且未被隔离的人数", M[-1])
    print("感染且被隔离的人数", MM[-1])
    print("尚未被感染的人数", N[-1])
