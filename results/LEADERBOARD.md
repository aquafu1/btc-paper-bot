# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 681 windows, 18850 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 355 | 34.4 | 35.0 | $-224.96 | -6.3% | $775.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1598 | 50.4 | 49.5 | $-428.83 | -2.7% | $571.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 870 | 38.4 | 39.2 | $-525.56 | -6.0% | $474.44 | -1.5 | done | can't tell from luck |
| trend_filter | 1098 | 50.4 | 50.9 | $-571.27 | -5.2% | $428.73 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1936 | 51.5 | 51.0 | $-614.66 | -3.2% | $385.34 | -1.4 | done | can't tell from luck |
| value_ev5 | 1308 | 40.6 | 41.2 | $-682.88 | -5.2% | $317.12 | -1.6 | done | can't tell from luck |
| coinflip | 2717 | 50.1 | 50.4 | $-1239.57 | -4.6% | $-239.57 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1598 | 49.6 | 51.3 | $-1241.26 | -7.8% | $-241.26 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1936 | 48.5 | 49.9 | $-1288.88 | -6.7% | $-288.88 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2717 | 50.8 | 51.8 | $-1450.89 | -5.3% | $-450.89 | -2.9 | done | losing for real |
| always_up | 2717 | 47.3 | 49.7 | $-2415.50 | -8.9% | $-1415.50 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4287 | 48.3 | 49.2 | $-2540.05 |
| ETH | 4698 | 48.3 | 48.6 | $-2808.19 |
| SOL | 4912 | 48.1 | 48.7 | $-2905.43 |
| XRP | 4953 | 48.5 | 48.4 | $-2430.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
