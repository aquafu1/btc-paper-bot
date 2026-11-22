# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 1:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1127 windows, 31165 settled trades, 21 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 594 | 34.7 | 35.2 | $-345.99 | -5.8% | $654.01 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3140 | 51.1 | 50.5 | $-834.38 | -2.7% | $165.62 | -1.5 | done | can't tell from luck |
| value_ev10 | 1456 | 38.3 | 39.2 | $-855.40 | -5.9% | $144.60 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2636 | 49.7 | 49.4 | $-1128.41 | -4.3% | $-128.41 | -2.2 | done | losing for real |
| value_ev5 | 2205 | 40.1 | 41.1 | $-1257.48 | -5.7% | $-257.48 | -2.3 | done | losing for real |
| trend_filter | 1849 | 49.1 | 50.4 | $-1438.45 | -7.8% | $-438.45 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2636 | 50.3 | 51.1 | $-1656.26 | -6.3% | $-656.26 | -3.3 | done | losing for real |
| coinflip | 4503 | 50.3 | 50.2 | $-1824.59 | -4.1% | $-824.59 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3140 | 48.9 | 50.2 | $-2082.71 | -6.6% | $-1082.71 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4503 | 50.3 | 51.4 | $-2702.24 | -6.0% | $-1702.24 | -4.2 | done | losing for real |
| always_up | 4503 | 47.7 | 49.3 | $-3429.00 | -7.6% | $-2429.00 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7146 | 48.3 | 49.0 | $-3637.02 |
| ETH | 7719 | 48.2 | 48.4 | $-4610.68 |
| SOL | 8114 | 48.0 | 48.4 | $-4588.97 |
| XRP | 8186 | 48.2 | 48.2 | $-4718.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
