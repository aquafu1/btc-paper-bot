# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 84 windows, 2138 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 330 | 56.4 | 50.9 | $+253.85 | +7.7% | $1253.85 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 156 | 59.0 | 52.8 | $+143.71 | +9.2% | $1143.71 | +1.2 | Wed 6:00 PM | too few trades (156/200) |
| reversal_15m_0.10pct | 203 | 56.2 | 52.1 | $+116.15 | +5.7% | $1116.15 | +0.8 | done | can't tell from luck |
| value_ev10 | 115 | 42.6 | 40.1 | $+6.88 | +0.6% | $1006.88 | +0.1 | Thu 3:30 AM | too few trades (115/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 4:00 PM | too few trades (43/200) |
| trend_filter | 116 | 47.4 | 48.7 | $-63.05 | -5.4% | $936.95 | -0.6 | Thu 3:15 AM | too few trades (116/200) |
| value_ev5 | 156 | 41.0 | 41.5 | $-88.55 | -5.7% | $911.45 | -0.6 | Wed 6:00 PM | too few trades (156/200) |
| coinflip | 330 | 50.3 | 51.5 | $-182.62 | -5.5% | $817.38 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 156 | 41.0 | 48.7 | $-283.47 | -18.2% | $716.53 | -2.2 | Wed 6:00 PM | too few trades (156/200) |
| momentum_15m_0.10pct | 203 | 43.8 | 49.5 | $-285.26 | -14.1% | $714.74 | -2.0 | done | losing for real |
| always_up | 330 | 47.0 | 50.1 | $-304.24 | -9.2% | $695.76 | -1.7 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 456 | 48.5 | 49.8 | $-74.10 |
| ETH | 514 | 47.7 | 48.6 | $-174.97 |
| SOL | 577 | 49.9 | 48.4 | $-180.92 |
| XRP | 591 | 49.7 | 48.6 | $-310.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
