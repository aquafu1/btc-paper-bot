# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 5:48 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 183 windows, 4709 settled trades, 0 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 346 | 59.8 | 53.0 | $+340.70 | +9.8% | $1340.70 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 456 | 57.7 | 52.4 | $+321.76 | +7.1% | $1321.76 | +1.6 | done | can't tell from luck |
| value_ev20 | 88 | 34.1 | 36.7 | $-128.58 | -14.6% | $871.42 | -1.1 | Sun 5:00 AM | too few trades (88/200) |
| momentum_5m_0.00pct | 732 | 51.4 | 51.3 | $-288.70 | -3.9% | $711.30 | -1.1 | done | can't tell from luck |
| value_ev10 | 237 | 37.6 | 40.7 | $-305.34 | -12.9% | $694.66 | -1.7 | done | can't tell from luck |
| coinflip | 732 | 50.4 | 50.9 | $-390.12 | -5.3% | $609.88 | -1.5 | done | can't tell from luck |
| value_ev5 | 348 | 39.1 | 42.4 | $-430.83 | -12.4% | $569.17 | -2.1 | done | losing for real |
| trend_filter | 236 | 41.1 | 49.4 | $-462.98 | -19.6% | $537.02 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 346 | 40.2 | 49.1 | $-744.94 | -21.5% | $255.06 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 456 | 42.3 | 49.7 | $-821.05 | -18.0% | $178.95 | -3.9 | done | losing for real |
| always_up | 732 | 46.7 | 50.1 | $-823.35 | -11.2% | $176.65 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1028 | 45.9 | 49.5 | $-1037.37 |
| ETH | 1170 | 46.1 | 48.8 | $-1268.83 |
| SOL | 1225 | 47.8 | 49.0 | $-1030.00 |
| XRP | 1286 | 50.1 | 49.1 | $-397.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
