# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 186 windows, 4745 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 348 | 59.8 | 53.0 | $+341.49 | +9.8% | $1341.49 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 461 | 57.5 | 52.4 | $+304.69 | +6.6% | $1304.69 | +1.5 | done | can't tell from luck |
| value_ev20 | 88 | 34.1 | 36.7 | $-128.58 | -14.6% | $871.42 | -1.1 | Sun 11:45 AM | too few trades (88/200) |
| momentum_5m_0.00pct | 738 | 51.6 | 51.3 | $-258.82 | -3.5% | $741.18 | -1.0 | done | can't tell from luck |
| value_ev10 | 238 | 37.4 | 40.7 | $-315.34 | -13.2% | $684.66 | -1.8 | done | can't tell from luck |
| coinflip | 738 | 50.4 | 50.9 | $-393.16 | -5.3% | $606.84 | -1.5 | done | can't tell from luck |
| value_ev5 | 350 | 38.9 | 42.5 | $-450.83 | -12.9% | $549.17 | -2.2 | done | losing for real |
| trend_filter | 237 | 41.4 | 49.4 | $-454.73 | -19.2% | $545.27 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 348 | 40.2 | 49.1 | $-746.81 | -21.5% | $253.19 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 461 | 42.5 | 49.7 | $-816.76 | -17.7% | $183.24 | -3.9 | done | losing for real |
| always_up | 738 | 46.5 | 50.1 | $-865.23 | -11.7% | $134.77 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1041 | 45.9 | 49.5 | $-1061.45 |
| ETH | 1181 | 46.1 | 48.8 | $-1292.13 |
| SOL | 1230 | 47.9 | 49.0 | $-1017.64 |
| XRP | 1293 | 50.0 | 49.2 | $-412.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
