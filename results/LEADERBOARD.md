# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 719 windows, 19810 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2029 | 51.7 | 50.8 | $-505.51 | -2.5% | $494.49 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1661 | 50.1 | 49.5 | $-562.73 | -3.4% | $437.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 912 | 38.0 | 39.1 | $-592.90 | -6.5% | $407.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 1373 | 40.7 | 41.1 | $-658.40 | -4.8% | $341.60 | -1.5 | done | can't tell from luck |
| trend_filter | 1159 | 50.2 | 50.9 | $-664.29 | -5.7% | $335.71 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1661 | 49.9 | 51.3 | $-1220.01 | -7.3% | $-220.01 | -3.1 | done | losing for real |
| coinflip | 2869 | 50.2 | 50.3 | $-1264.87 | -4.4% | $-264.87 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2029 | 48.3 | 50.0 | $-1449.39 | -7.1% | $-449.39 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2869 | 51.0 | 51.8 | $-1477.92 | -5.2% | $-477.92 | -2.9 | done | losing for real |
| always_up | 2869 | 47.3 | 49.5 | $-2487.40 | -8.7% | $-1487.40 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4487 | 48.1 | 49.1 | $-2802.11 |
| ETH | 4932 | 48.3 | 48.5 | $-2923.36 |
| SOL | 5165 | 48.1 | 48.7 | $-3063.12 |
| XRP | 5226 | 48.6 | 48.4 | $-2408.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
