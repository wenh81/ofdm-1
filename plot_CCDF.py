from pylab import *

lin_space = np.arange(0,6,0.2)
# err1 = np.loadtxt("BER_trained_at_0dB SNR")
# err2 = np.loadtxt("BER_trained_at_5dB SNR")
# err3 = np.loadtxt("BER_trained_at_10dB SNR")
# err4 = np.loadtxt("BER_trained_at_15dB SNR")
# err5 = np.loadtxt("BER_trained_at_20dB SNR")
# err6 = np.loadtxt("BER_trained_at_25dB SNR")
# err7 = np.loadtxt("BER_trained_at_30dB SNR")
# figure()
# semilogy(lin_space, err1 ,color='r',  marker="o", markersize=5,linewidth=2, label="BER_trained_at_0dB SNR")
# semilogy(lin_space, err2 ,color='g',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_5dB SNR")
# semilogy(lin_space, err3 ,color='b',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_10dB SNR")
# semilogy(lin_space, err4 ,color='yellow',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_15dB SNR")
# semilogy(lin_space, err5 ,color='r',  marker="^", markersize=5,linewidth=2,label="BER_trained_at_20dB SNR")
# semilogy(lin_space, err6 ,color='g',  marker="^", markersize=5,linewidth=2,label="BER_trained_at_25dB SNR")
# semilogy(lin_space, err7 ,color='b',  marker="^", markersize=5,linewidth=2,label="BER_trained_at_30dB SNR")
# legend()
# grid()


figure()

err1 = np.loadtxt("./result/CCDF_trained_at_15dB SNR_L4_64_rly")




# semilogy(lin_space, err1 ,color='r',  marker="o", markersize=5,linewidth=2, label="SER_trained_at_0dB SNR")
# semilogy(lin_space, err2 ,color='g',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_5dB SNR")
#semilogy(lin_space, err3 ,color='b',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR")
# semilogy(lin_space, err4 ,color='purple',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_15dB SNR")

semilogy(lin_space, err1 ,color='black',  marker="^", markersize=5,linewidth=2,label="CCDF_trained_at_8dB SNR_50000")





# semilogy(lin_space, err_scma ,color='red',  marker="s", markersize=5,linewidth=2,label="SER_trained_at_15dB SNR_conv")
# semilogy(lin_space, err5 ,color='r',  marker="^", markersize=5,linewidth=2,label="SER_trained_at_20dB SNR")
# semilogy(lin_space, err6 ,color='g',  marker="^", markersize=5,linewidth=2,label="SER_trained_at_25dB SNR")
# semilogy(lin_space, err7 ,color='b',  marker="^", markersize=5,linewidth=2,label="SER_trained_at_30dB SNR")
#semilogy(lin_space, err8 ,color='g',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_reg")
# semilogy(lin_space, err9 ,color='black',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_L1")
# semilogy(lin_space, err10 ,color='g',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_L2")
# semilogy(lin_space, err11 ,color='y',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_L3")
#semilogy(lin_space, err12 ,color='g',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_L4")
# semilogy(lin_space, err13 ,color='b',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_sparse")
# semilogy(lin_space, err14 ,color='black',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR_L4")
# semilogy(lin_space, err1 ,color='black',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_4.77dB SNR_L4")
# semilogy(lin_space, err2 ,color='b',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_6.77dB SNR_L4")
# semilogy(lin_space, err3 ,color='r',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_8.77dB SNR_L4")
# semilogy(lin_space, err4 ,color='g',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_10.77dB SNR_L4")
# semilogy(lin_space, err5 ,color='purple',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_12.77dB SNR_L4")
# semilogy(lin_space, err6 ,color='grey',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_14.77dB SNR_L4")
legend()
xlabel('PAPR0 [dB]', fontsize=12)
ylabel('CCDF (PAPR<PAPR0)', fontsize=12)
grid(which='minor')
grid(which='major')
show()
