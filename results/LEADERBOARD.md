# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 646 windows, 17848 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 336 | 34.5 | 35.3 | $-222.63 | -6.6% | $777.37 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1504 | 50.8 | 49.6 | $-283.57 | -1.9% | $716.43 | -0.7 | done | can't tell from luck |
| value_ev10 | 824 | 38.5 | 39.5 | $-549.91 | -6.7% | $450.09 | -1.6 | done | can't tell from luck |
| trend_filter | 1030 | 50.2 | 50.8 | $-568.76 | -5.5% | $431.24 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1838 | 51.4 | 51.0 | $-618.09 | -3.4% | $381.91 | -1.5 | done | can't tell from luck |
| value_ev5 | 1246 | 40.9 | 41.4 | $-631.64 | -5.1% | $368.36 | -1.5 | done | can't tell from luck |
| coinflip | 2576 | 50.2 | 50.5 | $-1171.45 | -4.5% | $-171.45 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1838 | 48.6 | 50.0 | $-1206.14 | -6.6% | $-206.14 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1504 | 49.2 | 51.4 | $-1313.37 | -8.7% | $-313.37 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2576 | 50.5 | 51.7 | $-1488.47 | -5.8% | $-488.47 | -3.0 | done | losing for real |
| always_up | 2576 | 47.4 | 49.7 | $-2210.33 | -8.6% | $-1210.33 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4050 | 48.3 | 49.3 | $-2416.43 |
| ETH | 4460 | 48.2 | 48.7 | $-2695.49 |
| SOL | 4637 | 48.0 | 48.8 | $-2880.26 |
| XRP | 4701 | 48.5 | 48.5 | $-2272.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
