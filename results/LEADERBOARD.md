# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 159 windows, 4047 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 294 | 59.5 | 53.4 | $+263.44 | +9.0% | $1263.44 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 390 | 56.2 | 52.5 | $+160.81 | +4.1% | $1160.81 | +0.9 | done | can't tell from luck |
| value_ev20 | 77 | 35.1 | 37.3 | $-98.86 | -12.8% | $901.14 | -0.9 | Sun 3:45 AM | too few trades (77/200) |
| momentum_5m_0.00pct | 628 | 52.2 | 51.2 | $-141.84 | -2.3% | $858.16 | -0.6 | done | can't tell from luck |
| value_ev10 | 206 | 37.9 | 40.9 | $-253.71 | -12.3% | $746.29 | -1.5 | done | can't tell from luck |
| coinflip | 628 | 50.8 | 50.9 | $-296.98 | -4.7% | $703.02 | -1.2 | done | can't tell from luck |
| trend_filter | 209 | 41.6 | 48.8 | $-373.00 | -17.8% | $627.00 | -2.6 | done | losing for real |
| value_ev5 | 303 | 38.9 | 42.6 | $-395.87 | -13.1% | $604.13 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 390 | 43.8 | 49.7 | $-581.88 | -14.9% | $418.12 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 294 | 40.5 | 48.9 | $-589.41 | -20.0% | $410.59 | -3.4 | done | losing for real |
| always_up | 628 | 45.9 | 50.3 | $-837.68 | -13.3% | $162.32 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 879 | 46.3 | 49.6 | $-755.76 |
| ETH | 1006 | 45.6 | 48.9 | $-1140.11 |
| SOL | 1063 | 48.1 | 49.0 | $-841.77 |
| XRP | 1099 | 50.2 | 49.2 | $-407.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
