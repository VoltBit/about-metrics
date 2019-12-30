
send_counter() {
  echo "bogus_metrics_counter:1|c" | nc -w 1 -u localhost 8125
}

send_gauge() {
  echo -n "bogus_metric_gauge:60|g|#shell" | nc -4u -w0 localhost 8125
}

send_gauge