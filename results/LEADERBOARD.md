# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 958 windows, 26532 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 487 | 35.1 | 34.9 | $-154.35 | -3.2% | $845.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1205 | 38.2 | 39.1 | $-659.22 | -5.5% | $340.78 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2710 | 51.3 | 50.6 | $-761.50 | -2.8% | $238.50 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2266 | 50.2 | 49.7 | $-861.20 | -3.8% | $138.80 | -1.8 | done | can't tell from luck |
| trend_filter | 1586 | 50.0 | 50.8 | $-1025.59 | -6.5% | $-25.59 | -2.6 | done | losing for real |
| value_ev5 | 1830 | 39.9 | 41.0 | $-1039.06 | -5.7% | $-39.06 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 2266 | 49.8 | 51.0 | $-1643.92 | -7.3% | $-643.92 | -3.5 | done | losing for real |
| coinflip | 3824 | 50.2 | 50.4 | $-1757.91 | -4.6% | $-757.91 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2710 | 48.7 | 50.2 | $-1893.92 | -7.0% | $-893.92 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3824 | 50.8 | 51.5 | $-1972.68 | -5.2% | $-972.68 | -3.3 | done | losing for real |
| always_up | 3824 | 46.9 | 49.6 | $-3754.30 | -9.8% | $-2754.30 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6046 | 48.2 | 49.0 | $-3455.26 |
| ETH | 6591 | 48.2 | 48.5 | $-4024.35 |
| SOL | 6923 | 48.2 | 48.6 | $-3850.23 |
| XRP | 6972 | 48.2 | 48.5 | $-4193.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
