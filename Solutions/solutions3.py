import time
time_start = time.time()

# PCA with 510 components done! Time elapsed: 1.7129957675933838 seconds
# Cumulative variance explained by 510 principal components: 0.9470420452326141
    
pca_510 = PCA(n_components=510)
pca_result_510 = pca_510.fit_transform(np_fps)

time_elapsed = time.time()-time_start

txt = 'PCA with 510 components done! Time elapsed: {} seconds'
print(txt.format(time_elapsed))

txt = 'Cumulative variance explained by 510 principal components: {}'
print(txt.format(np.sum(pca_510.explained_variance_ratio_)))

# t-SNE done! Time elapsed: 111.94909977912903 
time_start = time.time()

# The perplexity is related to the number of nearest neighbors that is 
# used in other manifold learning algorithms. 
# early_exaggeration float, optional (default: 12.0)
# Controls how tight natural clusters in the original space are 
# in the embedded space and how much space will be between them.
# Other things to try
# pca_tsne = TSNE(learning_rate=50, perplexity=50, early_exaggeration = 20.0, method = 'exact', n_components=3).fit_transform(pca_result_300)
# pca_tsne = TSNE(learning_rate=300, perplexity=50, early_exaggeration = 15.0, method = 'exact', n_components=3).fit_transform(pca_result_300)

pca_tsne = TSNE(learning_rate = 200, n_components=2).fit_transform(pca_result_510)
txt = 't-SNE done! Time elapsed: {} '
print(txt.format(time.time()-time_start))

xs = pca_tsne[:,0]
ys = pca_tsne[:,1]

plt.scatter(xs, ys, c = ys_fit, alpha = 0.5);