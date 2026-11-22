# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1126 windows, 31146 settled trades, 23 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 594 | 34.7 | 35.2 | $-345.99 | -5.8% | $654.01 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3139 | 51.2 | 50.5 | $-824.38 | -2.6% | $175.62 | -1.5 | done | can't tell from luck |
| value_ev10 | 1456 | 38.3 | 39.2 | $-855.40 | -5.9% | $144.60 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2636 | 49.7 | 49.4 | $-1128.41 | -4.3% | $-128.41 | -2.2 | done | losing for real |
| value_ev5 | 2203 | 40.1 | 41.1 | $-1237.48 | -5.6% | $-237.48 | -2.2 | done | losing for real |
| trend_filter | 1849 | 49.1 | 50.4 | $-1438.45 | -7.8% | $-438.45 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2636 | 50.3 | 51.1 | $-1656.26 | -6.3% | $-656.26 | -3.3 | done | losing for real |
| coinflip | 4498 | 50.4 | 50.2 | $-1792.68 | -4.0% | $-792.68 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3139 | 48.8 | 50.2 | $-2089.02 | -6.7% | $-1089.02 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4498 | 50.3 | 51.4 | $-2688.01 | -6.0% | $-1688.01 | -4.1 | done | losing for real |
| always_up | 4498 | 47.7 | 49.3 | $-3414.77 | -7.6% | $-2414.77 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7140 | 48.3 | 49.0 | $-3631.30 |
| ETH | 7715 | 48.2 | 48.4 | $-4606.04 |
| SOL | 8109 | 48.0 | 48.4 | $-4555.28 |
| XRP | 8182 | 48.2 | 48.2 | $-4678.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
