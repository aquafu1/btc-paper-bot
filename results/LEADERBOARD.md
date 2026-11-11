# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 86 windows, 2193 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 338 | 56.8 | 50.9 | $+285.49 | +8.4% | $1285.49 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 161 | 60.2 | 52.9 | $+184.25 | +11.4% | $1184.25 | +1.5 | Wed 5:45 PM | too few trades (161/200) |
| reversal_15m_0.10pct | 210 | 55.7 | 52.2 | $+95.60 | +4.6% | $1095.60 | +0.7 | done | can't tell from luck |
| value_ev10 | 116 | 42.2 | 40.1 | $-3.12 | -0.3% | $996.88 | -0.0 | Thu 4:00 AM | too few trades (116/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 6:15 PM | too few trades (43/200) |
| trend_filter | 119 | 47.1 | 48.7 | $-75.75 | -6.4% | $924.25 | -0.7 | Thu 3:00 AM | too few trades (119/200) |
| value_ev5 | 159 | 40.3 | 41.6 | $-118.55 | -7.5% | $881.45 | -0.8 | Wed 6:00 PM | too few trades (159/200) |
| coinflip | 338 | 50.0 | 51.5 | $-207.18 | -6.1% | $792.82 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 210 | 44.3 | 49.5 | $-280.04 | -13.3% | $719.96 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 161 | 39.8 | 48.7 | $-333.47 | -20.7% | $666.53 | -2.6 | Wed 5:45 PM | too few trades (161/200) |
| always_up | 338 | 46.2 | 50.1 | $-367.50 | -10.9% | $632.50 | -2.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 475 | 48.4 | 49.8 | $-104.09 |
| ETH | 531 | 47.1 | 48.6 | $-256.22 |
| SOL | 589 | 49.9 | 48.5 | $-185.27 |
| XRP | 598 | 49.7 | 48.6 | $-328.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
