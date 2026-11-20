# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 919 windows, 25391 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1160 | 38.2 | 39.1 | $-622.90 | -5.4% | $377.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2154 | 50.2 | 49.8 | $-842.00 | -3.9% | $158.00 | -1.8 | done | can't tell from luck |
| trend_filter | 1508 | 50.1 | 51.0 | $-988.22 | -6.6% | $11.78 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 2586 | 50.5 | 50.5 | $-1036.42 | -4.0% | $-36.42 | -2.0 | done | losing for real |
| value_ev5 | 1758 | 39.8 | 41.0 | $-1039.83 | -5.9% | $-39.83 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2586 | 49.5 | 50.3 | $-1428.57 | -5.5% | $-428.57 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2154 | 49.8 | 50.9 | $-1539.26 | -7.1% | $-539.26 | -3.4 | done | losing for real |
| coinflip | 3670 | 50.3 | 50.3 | $-1569.23 | -4.3% | $-569.23 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3670 | 51.1 | 51.6 | $-1790.83 | -4.9% | $-790.83 | -3.1 | done | losing for real |
| always_up | 3670 | 46.8 | 49.7 | $-3741.63 | -10.2% | $-2741.63 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5785 | 48.2 | 49.1 | $-3310.73 |
| ETH | 6311 | 48.2 | 48.5 | $-3902.63 |
| SOL | 6620 | 48.2 | 48.6 | $-3818.45 |
| XRP | 6675 | 48.3 | 48.5 | $-3712.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
