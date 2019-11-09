(for i in `seq 1 1000`; do
    echo -e "$RANDOM\t$RANDOM";
done )> random_keys.txt


(for i in `seq 1 1000`; do
    echo -e "$i\t$RANDOM";
done )> sorted_keys.txt

V = 'a'
(for i in `seq 1 1000`; do
    echo -e "$V\t$RANDOM";
done )> keys_not_in_table.txt
