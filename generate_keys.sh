(for i in `seq 1 1000`; do
    echo -e "$RANDOM\t$RANDOM";
done )> 1000_random_keys.txt


(for i in `seq 1 1000`; do
    echo -e "$i\t$RANDOM";
done )> 1000_sorted_keys.txt
