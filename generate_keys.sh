(for i in `seq 1 10000`; do
    echo -e "$RANDOM\t$RANDOM";
done )> random_keys.txt


(for i in `seq 1 10000`; do
    echo -e "$i\t$RANDOM";
done )> sorted_keys.txt
