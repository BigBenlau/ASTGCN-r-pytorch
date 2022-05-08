import numpy as np
import matplotlib.pyplot as plt
import argparse

def get_flow(file_name): # 将读取文件写成一个函数

    flow_data = np.load(file_name) # 载入交通流量数据
    print("The whole keys list of the npz file is:\n" ,[key for key in flow_data.keys()]) # 打印看看key是什么

    print("TThis npz file shape is:\n", flow_data["data"].shape)  # (16992, 307, 3)，16992是时间(59*24*12)，307是节点数，3表示每一维特征的维度（类似于二维的列）
    flow_data = flow_data['data'] # [T, N, D]，T为时间，N为节点数，D为节点特征

    return flow_data


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='data/PEMS04/PEMS04.npz', type=str,
                    help="show npz file path")
    args = parser.parse_args()
    traffic_data = get_flow(args.file)
    node_id = 22

    plt.plot(traffic_data[:24 * 48, node_id, 0])  # 0维特征
    plt.plot(traffic_data[:24 * 48, node_id, 1])  # 1维特征
    plt.plot(traffic_data[:24 * 48, node_id, 2])  # 2维特征

    plt.savefig("node_{:d}.png".format(node_id))
