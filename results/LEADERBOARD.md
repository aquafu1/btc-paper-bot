# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 134 windows, 3365 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 238 | 62.6 | 53.1 | $+365.16 | +15.3% | $1365.16 | +2.6 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 322 | 57.5 | 52.2 | $+246.63 | +7.7% | $1246.63 | +1.4 | done | can't tell from luck |
| momentum_5m_0.00pct | 528 | 52.1 | 51.0 | $-119.48 | -2.3% | $880.52 | -0.5 | done | can't tell from luck |
| value_ev20 | 62 | 25.8 | 36.4 | $-192.65 | -31.1% | $807.35 | -2.1 | Sun 10:00 AM | too few trades (62/200) |
| coinflip | 528 | 51.5 | 51.1 | $-210.94 | -4.0% | $789.06 | -1.0 | done | can't tell from luck |
| value_ev10 | 176 | 36.4 | 40.5 | $-252.46 | -14.3% | $747.54 | -1.6 | Thu 7:45 AM | too few trades (176/200) |
| trend_filter | 171 | 40.4 | 48.9 | $-351.43 | -20.6% | $648.57 | -2.7 | Thu 9:00 AM | too few trades (171/200) |
| value_ev5 | 252 | 36.9 | 42.0 | $-407.03 | -16.2% | $592.97 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 322 | 42.5 | 50.0 | $-574.16 | -17.8% | $425.84 | -3.3 | done | losing for real |
| momentum_60m_0.30pct | 238 | 37.4 | 49.1 | $-617.49 | -25.9% | $382.51 | -4.1 | done | losing for real |
| always_up | 528 | 46.2 | 50.2 | $-661.43 | -12.5% | $338.57 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 722 | 45.2 | 49.6 | $-839.82 |
| ETH | 834 | 44.7 | 48.7 | $-1014.99 |
| SOL | 890 | 48.7 | 48.7 | $-579.68 |
| XRP | 919 | 50.2 | 49.1 | $-340.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
