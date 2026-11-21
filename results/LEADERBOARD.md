# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 972 windows, 26971 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2755 | 51.3 | 50.5 | $-702.36 | -2.5% | $297.64 | -1.3 | done | can't tell from luck |
| value_ev10 | 1230 | 37.9 | 39.1 | $-754.80 | -6.1% | $245.20 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2305 | 50.3 | 49.8 | $-850.93 | -3.7% | $149.07 | -1.8 | done | can't tell from luck |
| value_ev5 | 1866 | 39.8 | 41.0 | $-1108.05 | -5.9% | $-108.05 | -2.2 | done | losing for real |
| trend_filter | 1613 | 49.8 | 50.9 | $-1117.85 | -6.9% | $-117.85 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2305 | 49.7 | 50.9 | $-1688.83 | -7.3% | $-688.83 | -3.6 | done | losing for real |
| coinflip | 3882 | 50.1 | 50.3 | $-1824.70 | -4.7% | $-824.70 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2755 | 48.7 | 50.3 | $-1994.56 | -7.2% | $-994.56 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3882 | 50.7 | 51.6 | $-2129.68 | -5.5% | $-1129.68 | -3.5 | done | losing for real |
| always_up | 3882 | 46.8 | 49.6 | $-3888.98 | -10.0% | $-2888.98 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6150 | 48.1 | 49.1 | $-3566.01 |
| ETH | 6699 | 48.0 | 48.5 | $-4305.08 |
| SOL | 7039 | 48.2 | 48.6 | $-3976.65 |
| XRP | 7083 | 48.1 | 48.4 | $-4432.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
