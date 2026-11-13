# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 269 windows, 7051 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 693 | 55.0 | 52.3 | $+81.64 | +1.2% | $1081.64 | +0.3 | done | can't tell from luck |
| value_ev20 | 126 | 34.9 | 36.9 | $-119.84 | -9.5% | $880.16 | -0.8 | Sun 9:45 AM | too few trades (126/200) |
| reversal_60m_0.30pct | 561 | 52.9 | 52.3 | $-156.75 | -2.8% | $843.25 | -0.7 | done | can't tell from luck |
| value_ev10 | 338 | 37.6 | 40.8 | $-380.84 | -11.3% | $619.16 | -1.8 | done | can't tell from luck |
| trend_filter | 367 | 46.3 | 50.1 | $-438.42 | -11.9% | $561.58 | -2.3 | done | losing for real |
| value_ev5 | 499 | 39.9 | 42.4 | $-494.88 | -9.9% | $505.12 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 561 | 47.1 | 49.6 | $-561.95 | -10.0% | $438.05 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1071 | 50.0 | 51.4 | $-741.32 | -6.9% | $258.68 | -2.4 | done | losing for real |
| coinflip | 1071 | 49.3 | 50.9 | $-782.90 | -7.3% | $217.10 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 693 | 45.0 | 49.7 | $-913.02 | -13.2% | $86.98 | -3.5 | done | losing for real |
| always_up | 1071 | 47.4 | 50.2 | $-1042.65 | -9.7% | $-42.65 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1564 | 46.4 | 49.6 | $-1637.52 |
| ETH | 1761 | 46.9 | 49.0 | $-1706.21 |
| SOL | 1829 | 48.3 | 49.3 | $-1372.25 |
| XRP | 1897 | 49.0 | 49.1 | $-834.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
