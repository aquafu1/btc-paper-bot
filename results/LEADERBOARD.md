# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1117 windows, 30920 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 590 | 34.6 | 35.1 | $-349.77 | -5.9% | $650.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3119 | 51.1 | 50.5 | $-858.91 | -2.8% | $141.09 | -1.5 | done | can't tell from luck |
| value_ev10 | 1442 | 38.1 | 39.1 | $-890.86 | -6.2% | $109.14 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2624 | 49.8 | 49.4 | $-1067.73 | -4.1% | $-67.73 | -2.1 | done | losing for real |
| value_ev5 | 2183 | 40.0 | 41.0 | $-1256.70 | -5.8% | $-256.70 | -2.3 | done | losing for real |
| trend_filter | 1833 | 49.2 | 50.4 | $-1381.61 | -7.5% | $-381.61 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2624 | 50.2 | 51.1 | $-1713.61 | -6.5% | $-713.61 | -3.4 | done | losing for real |
| coinflip | 4462 | 50.4 | 50.2 | $-1770.60 | -4.0% | $-770.60 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3119 | 48.9 | 50.2 | $-2052.07 | -6.6% | $-1052.07 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4462 | 50.5 | 51.4 | $-2526.32 | -5.7% | $-1526.32 | -3.9 | done | losing for real |
| always_up | 4462 | 47.7 | 49.3 | $-3432.97 | -7.7% | $-2432.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7087 | 48.3 | 49.0 | $-3616.45 |
| ETH | 7656 | 48.1 | 48.4 | $-4609.02 |
| SOL | 8048 | 48.0 | 48.4 | $-4540.72 |
| XRP | 8129 | 48.3 | 48.2 | $-4534.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
