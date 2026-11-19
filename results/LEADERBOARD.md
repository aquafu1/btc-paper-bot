# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 805 windows, 22112 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 411 | 33.6 | 35.0 | $-321.28 | -7.8% | $678.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1011 | 38.0 | 39.2 | $-644.51 | -6.4% | $355.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1857 | 50.1 | 49.6 | $-722.35 | -3.9% | $277.65 | -1.7 | done | can't tell from luck |
| trend_filter | 1294 | 50.2 | 50.8 | $-781.84 | -6.0% | $218.16 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2259 | 51.0 | 50.6 | $-801.50 | -3.5% | $198.50 | -1.7 | done | can't tell from luck |
| value_ev5 | 1528 | 40.2 | 41.1 | $-855.55 | -5.6% | $144.45 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1857 | 49.9 | 51.2 | $-1328.51 | -7.2% | $-328.51 | -3.2 | done | losing for real |
| coinflip | 3212 | 50.2 | 50.3 | $-1370.36 | -4.3% | $-370.36 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 3212 | 51.3 | 51.6 | $-1376.83 | -4.3% | $-376.83 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2259 | 49.0 | 50.2 | $-1380.32 | -6.1% | $-380.32 | -2.9 | done | losing for real |
| always_up | 3212 | 47.4 | 49.6 | $-2766.99 | -8.6% | $-1766.99 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5022 | 48.3 | 49.1 | $-2805.14 |
| ETH | 5510 | 48.1 | 48.5 | $-3487.26 |
| SOL | 5759 | 48.3 | 48.6 | $-3175.15 |
| XRP | 5821 | 48.5 | 48.5 | $-2882.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
