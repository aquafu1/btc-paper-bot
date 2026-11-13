# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 189 windows, 4843 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 354 | 59.9 | 53.1 | $+345.29 | +9.8% | $1345.29 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 471 | 57.7 | 52.4 | $+329.78 | +7.0% | $1329.78 | +1.6 | done | can't tell from luck |
| value_ev20 | 92 | 32.6 | 36.9 | $-168.58 | -18.3% | $831.42 | -1.5 | Sun 8:30 AM | too few trades (92/200) |
| momentum_5m_0.00pct | 751 | 51.8 | 51.4 | $-244.29 | -3.3% | $755.71 | -0.9 | done | can't tell from luck |
| value_ev10 | 244 | 36.9 | 40.8 | $-353.19 | -14.5% | $646.81 | -2.0 | done | can't tell from luck |
| coinflip | 751 | 50.3 | 50.9 | $-420.97 | -5.6% | $579.03 | -1.6 | done | can't tell from luck |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 361 | 39.1 | 42.6 | $-460.29 | -12.8% | $539.71 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 354 | 40.1 | 49.0 | $-767.67 | -21.7% | $232.33 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 471 | 42.3 | 49.7 | $-863.22 | -18.3% | $136.78 | -4.1 | done | losing for real |
| always_up | 751 | 46.2 | 50.2 | $-931.43 | -12.4% | $68.57 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1055 | 46.1 | 49.5 | $-1061.41 |
| ETH | 1208 | 46.0 | 48.8 | $-1346.13 |
| SOL | 1257 | 47.8 | 49.1 | $-1058.52 |
| XRP | 1323 | 49.7 | 49.2 | $-525.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
