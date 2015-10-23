
[REGEX]




























# [customdomain]: ../articles/app-service-web/web-sites-custom-domain-name.md
(\[[^\[|^\]]*\]:\s*)\.\.\/articles\/(?!includes|media)([^\/]+)\/([^\/]*)\.md/? = \1\3

# [customdomain](../articles/app-service-web/web-sites-custom-domain-name.md)
(\[[^\[|^\]]*\]\s*)\(\.\.\/articles?\/(?!includes|media)([^\/]+)\/([^\/]*)\.md/?\) = \1(\3)

# [customdomain]: ../articles/app-service-web/web-sites-custom-domain-name.md#test
(\[[^\[|^\]]*\]:\s*)\.\.\/articles\/(?!includes|media)([^\/]+)\/([^\/]*)\.md(\#[^\/]*)/? = \1\3\4

# [customdomain](../articles/app-service-web/web-sites-custom-domain-name.md#test)
(\[[^\[|^\]]*\]\s*)\((\.\.\/articles?\/)?(?!includes|media)([^\/]+)\/([^\/]*)\.md(\#[^\/]*)/?\) = \1(\4\5)

# [xxxxxxxxxxxx]: xxxx-xxxx-xxxx.md = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx
(\[[^\[|^\]]*\]:\s*)([^\/]*)\.md/? = \1\2
# [xxxxxxxxxxxx]: ../xxxx/xxxx-xxxx-xxxx.md = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx
(\[[^\[|^\]]*\]:\s*)\.\.\/([^\/]*)\.md/? = \1\2

# [1]: ../HDInsight/hdinsight-hadoop-visual-studio-tools-get-started.md
(\[[^\[|^\]]*\]:\s*)\.\.\/(?!includes|media)([^\/]+)\/([^\/]*)\.md/? = \1\3

# [1](../HDInsight/hdinsight-hadoop-visual-studio-tools-get-started.md)
(\[[^\[|^\]]*\]\s*)\(\.\.\/(?!includes|media)([^\/]+)\/([^\/]*)\.md/?\) = \1(\3)

# [xxxxxxxxxxxx]: ../xxxx-xxxx-xxxx.md#xxxx = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx#xxxx
(\[[^\[|^\]]*\]:\s*)\.\.\/([^\/]*)\.md/?(\#[^\/]*)/? = \1\2\3

# [xxxxxxxxxxxx]: ../xxxx/xxxx-xxxx-xxxx.md#xxxx = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx#xxxx
(\[[^\[|^\]]*\]:\s*)\.\.\/(?!includes|media)([^\/]+)\/([^\/]*)\.md/?(\#[^\/]*)/?  = \1\3\4

# [1](../HDInsight/hdinsight-hadoop-visual-studio-tools-get-started.md)
(\[[^\[|^\]]*\]\s*)\(\.\.\/(?!includes|media)([^\/]+)\/([^\/]*)\.md/?(\#[^\/]*)/?\) = \1(\3\4)

\(\/documentation\/articles\/([^\/]*).md/?\) = (/documentation/articles/\1)

# (../xxxx-xxxxxx-xxxxx/) = (/documentation/articles/xxxx-xxxxxx-xxxxx/)
\(\.\.\/([^\/]*)\/?\) = (/documentation/articles/\1)

# (../xxxx-xxxxxx-xxxxx.md/) = (/documentation/articles/xxxx-xxxxxx-xxxxx/)
\(\.\.\/([^\/]*).md\/?\) = (/documentation/articles/\1)

# [xxxxxxxxxxxx]: ../xxxx/xxxx-xxxx-xxxx = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx
(\[[^\[|^\]]*\]:\s*)\.\.\/(?!includes|media)([^\/]*)/(?!#[^\/]*)([^\/]*)/? = \1\3

# [1]: ../HDInsight/hdinsight-hadoop-visual-studio-tools-get-started
(\[[^\[|^\]]*\]:\s*)\.\.\/(?!includes|media)([^\/]+)\/([^\/]*)/? = \1\3

# [Create, manage, or delete a storage account](../storage-create-storage-account/#replication-options)
(\[[^\[|^\]]*\]\s*)\(\.\.\/(?!includes|media)([^\/]+)\/#([^\/]*)/?\) = \1(\2#\3)

# [1](../HDInsight/hdinsight-hadoop-visual-studio-tools-get-started)
(\[[^\[|^\]]*\]\s*)\(\.\.\/(?!includes|media)([^\/]+)\/(?!#[^\/]*)([^\/]*)/?\) = \1(\3)

# [xxxxxxxxxxxx]: ../xxxx-xxxx-xxxx#xxxx = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx#xxxx
(\[[^\[|^\]]*\]:\s*)\.\.\/([^\/]*)(\#[^\/]*)/? = \1\2\3

# [xxxxxxxxxxxx]: ../xxxx/xxxx-xxxx-xxxx#xxxx = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx#xxxx
(\[[^\[|^\]]*\]:\s*)\.\.\/(?!includes|media)([^\/]+)\/([^\/|^\.]*)(\#[^\/]*)/?  = \1\3\4

# [1](../HDInsight/hdinsight-hadoop-visual-studio-tools-get-started)
(\[[^\[|^\]]*\]\s*)\(\.\.\/(?!includes|media)([^\/]+)\/([^\/|^\.]*)(\#[^\/]*)/?\) = \1(\3\4)

#[link text](xxx-xxx-xxx.md#xxx-xxx) = 	[link text](/documentation/articles/xxx-xxx-xxx#xxx-xxx)
(\[.*?\]\s*\()(\.\.\/)?([^\/]*?)(\.md)/?#([^\/]*?)/?(\)) = \1/documentation/articles/\3#\5\6

#[link text](/documentation/articles/xxx-xxx-xxx.md#xxx-xxx) = 	[link text](/documentation/articles/xxx-xxx-xxx#xxx-xxx)
(\[.*?\]\s*\()/documentation/articles/([^\/]*?)(\.md)/?#([^\/]*?)/?(\)) = \1/documentation/articles/\2#\4\5

# [setcname1]: ../media/dncmntask-cname-5.png

/documentation/articles/# = #






















hdinsight-high-availability-linux = hdinsight-high-availability
hdinsight-hadoop-customize-cluster-linux = hdinsight-hadoop-customize-cluster
hdinsight-storm-deploy-monitor-topology-linux = hdinsight-storm-deploy-monitor-topology
hdinsight-apache-storm-tutorial-get-started-linux = hdinsight-apache-storm-tutorial-get-started

hdinsight-use-sqoop-mac-linux = hdinsight-use-sqoop
hdinsight-hadoop-provision-linux-clusters = hdinsight-provision-clusters



# [xxxxxxxxxxxx]: xxxx-xxxx-xxxx.md = [xxxxxxxxxxxx]: xxxx-xxxx-xxxx
(\[[^\[|^\]]*\]:\s*)([\w|\-]*)\.md = \1\2


# href="../networking/virtual-networks-overview.md"
href{equal}"\.\./[\w|\-]+/([\w|\-]*)\.md" = href{equal}"/documentation/articles/\1"

\.\./documentation/services/ = /documentation/services/


