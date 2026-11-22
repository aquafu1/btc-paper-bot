# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1063 windows, 29425 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2978 | 51.2 | 50.4 | $-782.32 | -2.6% | $217.68 | -1.4 | done | can't tell from luck |
| value_ev10 | 1359 | 37.7 | 39.2 | $-927.80 | -6.8% | $72.20 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2503 | 49.8 | 49.6 | $-1115.05 | -4.5% | $-115.05 | -2.2 | done | losing for real |
| trend_filter | 1754 | 49.5 | 50.7 | $-1278.85 | -7.3% | $-278.85 | -3.1 | done | losing for real |
| value_ev5 | 2065 | 39.8 | 41.0 | $-1309.38 | -6.3% | $-309.38 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2503 | 50.2 | 51.0 | $-1612.04 | -6.4% | $-612.04 | -3.3 | done | losing for real |
| coinflip | 4246 | 50.4 | 50.3 | $-1731.73 | -4.1% | $-731.73 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2978 | 48.8 | 50.3 | $-2076.21 | -7.0% | $-1076.21 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4246 | 50.9 | 51.5 | $-2162.50 | -5.1% | $-1162.50 | -3.4 | done | losing for real |
| always_up | 4246 | 47.2 | 49.4 | $-3765.13 | -8.9% | $-2765.13 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6720 | 48.4 | 49.0 | $-3448.68 |
| ETH | 7282 | 48.1 | 48.5 | $-4597.28 |
| SOL | 7674 | 48.1 | 48.5 | $-4436.23 |
| XRP | 7749 | 48.2 | 48.3 | $-4589.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
