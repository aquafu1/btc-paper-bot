# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 158 windows, 4013 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 290 | 59.3 | 53.3 | $+252.95 | +8.7% | $1252.95 | +1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 387 | 56.6 | 52.6 | $+190.81 | +4.9% | $1190.81 | +1.0 | done | can't tell from luck |
| value_ev20 | 77 | 35.1 | 37.3 | $-98.86 | -12.8% | $901.14 | -0.9 | Sun 3:15 AM | too few trades (77/200) |
| momentum_5m_0.00pct | 624 | 52.4 | 51.2 | $-123.21 | -2.0% | $876.79 | -0.5 | done | can't tell from luck |
| value_ev10 | 204 | 37.7 | 40.8 | $-250.44 | -12.3% | $749.56 | -1.5 | done | can't tell from luck |
| coinflip | 624 | 50.8 | 50.9 | $-294.54 | -4.7% | $705.46 | -1.2 | done | can't tell from luck |
| trend_filter | 205 | 42.0 | 48.9 | $-354.36 | -17.3% | $645.64 | -2.4 | done | losing for real |
| value_ev5 | 301 | 38.9 | 42.5 | $-392.61 | -13.0% | $607.39 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 290 | 40.7 | 49.0 | $-570.78 | -19.7% | $429.22 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 387 | 43.4 | 49.7 | $-607.53 | -15.7% | $392.47 | -3.1 | done | losing for real |
| always_up | 624 | 45.7 | 50.3 | $-848.17 | -13.6% | $151.83 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 869 | 46.3 | 49.5 | $-762.59 |
| ETH | 996 | 45.6 | 48.9 | $-1123.79 |
| SOL | 1055 | 48.2 | 48.9 | $-814.44 |
| XRP | 1093 | 50.2 | 49.2 | $-395.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
