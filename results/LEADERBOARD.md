# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1138 windows, 31432 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 603 | 34.7 | 35.2 | $-365.66 | -6.1% | $634.34 | -1.1 | done | can't tell from luck |
| value_ev10 | 1472 | 38.2 | 39.2 | $-902.14 | -6.1% | $97.86 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3162 | 50.9 | 50.5 | $-967.56 | -3.1% | $32.44 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2654 | 49.7 | 49.4 | $-1143.40 | -4.3% | $-143.40 | -2.2 | done | losing for real |
| value_ev5 | 2228 | 40.1 | 41.1 | $-1295.98 | -5.8% | $-295.98 | -2.3 | done | losing for real |
| trend_filter | 1865 | 49.1 | 50.5 | $-1451.78 | -7.8% | $-451.78 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2654 | 50.3 | 51.1 | $-1666.84 | -6.3% | $-666.84 | -3.3 | done | losing for real |
| coinflip | 4544 | 50.3 | 50.2 | $-1856.85 | -4.1% | $-856.85 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3162 | 49.1 | 50.2 | $-1976.95 | -6.3% | $-976.95 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4544 | 50.3 | 51.4 | $-2785.30 | -6.1% | $-1785.30 | -4.3 | done | losing for real |
| always_up | 4544 | 47.8 | 49.3 | $-3427.40 | -7.5% | $-2427.40 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7203 | 48.4 | 49.0 | $-3664.03 |
| ETH | 7790 | 48.2 | 48.4 | $-4618.37 |
| SOL | 8183 | 48.0 | 48.4 | $-4629.03 |
| XRP | 8256 | 48.1 | 48.3 | $-4928.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
