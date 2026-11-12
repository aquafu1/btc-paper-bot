# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 178 windows, 4552 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 443 | 58.0 | 52.3 | $+345.86 | +7.8% | $1345.86 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 336 | 59.5 | 53.1 | $+309.43 | +9.2% | $1309.43 | +1.8 | done | can't tell from luck |
| value_ev20 | 87 | 33.3 | 36.6 | $-143.13 | -16.5% | $856.87 | -1.3 | Sun 2:15 AM | too few trades (87/200) |
| momentum_5m_0.00pct | 704 | 51.1 | 51.3 | $-310.65 | -4.4% | $689.35 | -1.2 | done | can't tell from luck |
| value_ev10 | 228 | 36.8 | 40.5 | $-322.61 | -14.1% | $677.39 | -1.9 | done | can't tell from luck |
| coinflip | 704 | 50.4 | 50.9 | $-383.10 | -5.4% | $616.90 | -1.5 | done | can't tell from luck |
| trend_filter | 230 | 41.3 | 49.3 | $-437.61 | -19.0% | $562.39 | -2.9 | done | losing for real |
| value_ev5 | 337 | 38.6 | 42.3 | $-449.47 | -13.3% | $550.53 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 336 | 40.5 | 49.0 | $-694.72 | -20.7% | $305.28 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 443 | 42.0 | 49.7 | $-830.22 | -18.7% | $169.78 | -4.0 | done | losing for real |
| always_up | 704 | 46.2 | 49.9 | $-846.05 | -12.0% | $153.95 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 990 | 45.9 | 49.4 | $-991.79 |
| ETH | 1136 | 45.6 | 48.8 | $-1366.53 |
| SOL | 1188 | 47.6 | 48.9 | $-1069.88 |
| XRP | 1238 | 50.1 | 49.0 | $-334.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
