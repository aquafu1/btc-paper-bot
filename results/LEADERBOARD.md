# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 158 windows, 4023 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 291 | 59.1 | 53.3 | $+242.95 | +8.3% | $1242.95 | +1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 388 | 56.4 | 52.6 | $+180.81 | +4.7% | $1180.81 | +1.0 | done | can't tell from luck |
| value_ev20 | 77 | 35.1 | 37.3 | $-98.86 | -12.8% | $901.14 | -0.9 | Sun 3:45 AM | too few trades (77/200) |
| momentum_5m_0.00pct | 625 | 52.5 | 51.2 | $-111.84 | -1.8% | $888.16 | -0.5 | done | can't tell from luck |
| value_ev10 | 205 | 37.6 | 40.8 | $-260.44 | -12.7% | $739.56 | -1.6 | done | can't tell from luck |
| coinflip | 625 | 50.9 | 50.9 | $-283.18 | -4.5% | $716.82 | -1.2 | done | can't tell from luck |
| trend_filter | 206 | 42.2 | 48.9 | $-343.00 | -16.7% | $657.00 | -2.4 | done | losing for real |
| value_ev5 | 302 | 38.7 | 42.6 | $-402.61 | -13.3% | $597.39 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 291 | 40.9 | 49.0 | $-559.41 | -19.2% | $440.59 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 388 | 43.6 | 49.6 | $-596.17 | -15.4% | $403.83 | -3.1 | done | losing for real |
| always_up | 625 | 45.6 | 50.3 | $-858.17 | -13.7% | $141.83 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 879 | 46.3 | 49.6 | $-755.76 |
| ETH | 996 | 45.6 | 48.9 | $-1123.79 |
| SOL | 1055 | 48.2 | 48.9 | $-814.44 |
| XRP | 1093 | 50.2 | 49.2 | $-395.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
