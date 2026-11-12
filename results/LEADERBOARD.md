# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 169 windows, 4331 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 320 | 60.9 | 53.3 | $+383.96 | +12.0% | $1383.96 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 421 | 58.0 | 52.7 | $+322.29 | +7.7% | $1322.29 | +1.7 | done | can't tell from luck |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 6:00 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 668 | 52.1 | 51.2 | $-148.50 | -2.2% | $851.50 | -0.6 | done | can't tell from luck |
| value_ev10 | 219 | 37.9 | 40.8 | $-261.47 | -11.9% | $738.53 | -1.5 | done | can't tell from luck |
| coinflip | 668 | 50.1 | 51.0 | $-389.42 | -5.8% | $610.58 | -1.6 | done | can't tell from luck |
| value_ev5 | 323 | 39.0 | 42.5 | $-401.11 | -12.4% | $598.89 | -2.0 | done | can't tell from luck |
| trend_filter | 223 | 40.4 | 49.1 | $-452.69 | -20.3% | $547.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 320 | 39.1 | 48.9 | $-733.80 | -22.9% | $266.20 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 421 | 42.0 | 49.5 | $-757.00 | -18.0% | $243.00 | -3.7 | done | losing for real |
| always_up | 668 | 46.3 | 50.0 | $-775.51 | -11.6% | $224.49 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 939 | 46.0 | 49.5 | $-876.70 |
| ETH | 1078 | 45.7 | 48.9 | $-1185.57 |
| SOL | 1138 | 48.1 | 49.0 | $-866.35 |
| XRP | 1176 | 50.0 | 49.1 | $-386.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
