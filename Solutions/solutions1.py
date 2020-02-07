## Warning: core i7 Windows OS this chunk took 
# t-SNE with LR=50, n_comp = 3! Time elapsed: 86.90082573890686 seconds

time_start = time.time()

model = TSNE(learning_rate=50, n_components=3)
transformed = model.fit_transform(np_fps)

xs = transformed[:,0]
ys = transformed[:,1]

time_elapsed = time.time()-time_start
txt = 't-SNE with LR=50, n_comp = 3! Time elapsed: {} seconds'
print(txt.format(time_elapsed))

plt.scatter(xs, ys, c = ys_fit, alpha = 0.5);
