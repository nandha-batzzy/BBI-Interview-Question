#ANS 1
SELECT count(user_id),visit_date as us from visits_transactions.visits
GROUP BY visit_date
LIMIT 1;

#ANS 2
SELECT amount,transaction_date from visits_transactions.transactions
ORDER BY amount DESC
LIMIT 1;

#ANS 3
SELECT amount,Tuser_id from visits_transactions.transactions
ORDER BY amount DESC
LIMIT 1;

#ANS 4
SELECT AVG(amout) as Average from visits_transactions.transactions;

#ANS 5
SELECT user_id from visits_transactions.visits
LEFT JOIN visits_transactions.transactions ON user_id = Tuser_id
WHERE amount IS NULL;
