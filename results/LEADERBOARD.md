# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1268 windows, 34173 settled trades, 413 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 666 | 34.1 | 35.3 | $-534.16 | -8.0% | $465.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1636 | 38.5 | 39.2 | $-888.51 | -5.4% | $111.49 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3427 | 50.7 | 50.2 | $-1200.75 | -3.5% | $-200.75 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2869 | 49.5 | 49.4 | $-1304.67 | -4.5% | $-304.67 | -2.4 | done | losing for real |
| value_ev5 | 2476 | 40.4 | 41.1 | $-1331.48 | -5.4% | $-331.48 | -2.3 | done | losing for real |
| trend_filter | 2025 | 49.0 | 50.4 | $-1618.74 | -8.0% | $-618.74 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2869 | 50.5 | 51.0 | $-1692.95 | -5.9% | $-692.95 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3427 | 49.3 | 50.2 | $-2036.54 | -5.9% | $-1036.54 | -3.5 | done | losing for real |
| coinflip | 4926 | 50.0 | 50.1 | $-2248.63 | -4.6% | $-1248.63 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4926 | 50.4 | 51.4 | $-2838.03 | -5.8% | $-1838.03 | -4.2 | done | losing for real |
| always_up | 4926 | 47.9 | 49.4 | $-3622.85 | -7.4% | $-2622.85 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8109 | 48.0 | 48.9 | $-4821.86 |
| ETH | 8754 | 48.2 | 48.3 | $-4911.20 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
