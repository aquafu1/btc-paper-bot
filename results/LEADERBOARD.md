# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 165 windows, 4226 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 311 | 60.1 | 53.3 | $+320.33 | +10.3% | $1320.33 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 409 | 57.2 | 52.7 | $+242.11 | +5.9% | $1242.11 | +1.3 | done | can't tell from luck |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 3:30 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 652 | 52.3 | 51.1 | $-117.13 | -1.8% | $882.87 | -0.5 | done | can't tell from luck |
| value_ev10 | 217 | 38.2 | 40.7 | $-241.47 | -11.1% | $758.53 | -1.4 | done | can't tell from luck |
| value_ev5 | 317 | 39.4 | 42.4 | $-361.73 | -11.4% | $638.27 | -1.8 | done | can't tell from luck |
| coinflip | 652 | 50.3 | 51.0 | $-368.47 | -5.7% | $631.53 | -1.5 | done | can't tell from luck |
| trend_filter | 216 | 40.7 | 48.9 | $-419.61 | -19.4% | $580.39 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 311 | 39.9 | 48.8 | $-662.13 | -21.3% | $337.87 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 409 | 42.8 | 49.4 | $-673.26 | -16.5% | $326.74 | -3.4 | done | losing for real |
| always_up | 652 | 46.2 | 50.0 | $-779.27 | -12.0% | $220.73 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 917 | 46.1 | 49.4 | $-825.96 |
| ETH | 1055 | 45.8 | 48.8 | $-1152.66 |
| SOL | 1108 | 48.0 | 48.9 | $-865.81 |
| XRP | 1146 | 50.3 | 49.0 | $-318.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
