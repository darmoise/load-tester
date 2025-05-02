(import json)
(import time :as t)
(import kafka :as kafka)

(def producer
  (KafkaProducer kafka
    {"bootstrap_servers" "localhost:9092"
     "value_serializer" (fn [v] (.encode (dumps v) "utf-8"))}))

(defn send-messages [topic msg rate duration]
  (setv interval (/ 1 rate)
        end-time (+ (t/time) duration)
        sent 0)

  (while (< (t/time) end-time)
    (.send producer topic msg)
    (+= sent 1)
    (t/sleep interval))

  (.flush producer)
  (.close producer)
  (print "Sent {sent} messages in {duration} seconds."))

(defn -main []
  (setv msg {"event" "test"
             "timestamp" (int (t/time))})
  (send-messages "my-topic" msg 500 10))

(-main)
