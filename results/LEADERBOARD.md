# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1130 windows, 31220 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 596 | 34.6 | 35.2 | $-365.99 | -6.1% | $634.01 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3143 | 51.1 | 50.5 | $-844.07 | -2.7% | $155.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1459 | 38.2 | 39.2 | $-885.40 | -6.1% | $114.60 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2638 | 49.7 | 49.4 | $-1116.63 | -4.2% | $-116.63 | -2.2 | done | losing for real |
| value_ev5 | 2210 | 40.0 | 41.1 | $-1287.18 | -5.8% | $-287.18 | -2.3 | done | losing for real |
| trend_filter | 1851 | 49.1 | 50.4 | $-1426.67 | -7.7% | $-426.67 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2638 | 50.3 | 51.1 | $-1676.26 | -6.4% | $-676.26 | -3.4 | done | losing for real |
| coinflip | 4514 | 50.4 | 50.2 | $-1770.59 | -3.9% | $-770.59 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3143 | 48.9 | 50.2 | $-2080.93 | -6.6% | $-1080.93 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4514 | 50.3 | 51.4 | $-2748.02 | -6.1% | $-1748.02 | -4.2 | done | losing for real |
| always_up | 4514 | 47.7 | 49.4 | $-3506.57 | -7.8% | $-2506.57 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7152 | 48.3 | 49.0 | $-3656.84 |
| ETH | 7731 | 48.1 | 48.4 | $-4659.18 |
| SOL | 8128 | 48.0 | 48.4 | $-4628.00 |
| XRP | 8209 | 48.2 | 48.2 | $-4764.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
